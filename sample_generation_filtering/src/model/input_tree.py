from .input_tree_node import Node
import helper_functions as hf
import random
from collections import deque
import re
import copy

class InputTree:

    def __init__(self, grammar, seed, verbose):
        """ Constructs a message tree object.

        Args:
          grammar: input grammar for describing the structure
          seed: a value based on which random number is
            generated. It is used for reproducibility.
          verbose: a parameter to decide whether information
            should be displayed.

        Returns:
          the constructed object
        """
        self.nonterminal_node_list = {}
        Node.symbol_counts = {}
        self.root = Node('<start>', None)
        self.grammar = grammar
        self.seed = seed
        random.seed(seed)
        self.verbose = verbose

        self.max_nesting_depth = 2
        self.att_list = []

    def build_tree(self, start_node: Node, mode=0):
        # mode=0 样例构造  mode=1 样例变异

        multipart_entity_flag = False       # Content-Type选择为multipart时置位 仅用于在决定entity-body的扩展结果时加以控制
        boundary_stack = deque()            # 维护有效的boundary集合 栈顶元素是当前multipart的boundary
        nesting_depth = 0                   # 每个multipart body的出现就意味着一次嵌套 对于嵌套的深度有一定限制

        self.nonterminal_node_list[start_node.id] = start_node

        node_queue = deque([start_node])

        while node_queue:
            # (1) 取队头节点 选择一组扩展方式
            current_node = node_queue.pop()

            # For Debug
            if current_node.symbol == "<body-part>":
                debug_mode = True

            symbol_list = []
            # if current_node.symbol == "<entity-headers>" and nesting_depth == 0:
            #     # 最外层不设Content-Disposition
            #     symbol_list = ["<content_CRLF>", "<encoding_CRLF>", "<id_CRLF>"]
            if current_node.symbol == "<C_type_subtype>" and nesting_depth >= self.max_nesting_depth:
                # 递归深度达到极限
                symbol_list = self.get_expansion_result(current_node, exclusion=["<multipart>"])
            elif (current_node.symbol == "<encoding_CRLF>" or current_node.symbol == "<disposition_CRLF>") and multipart_entity_flag is True:
                # Content-Type已经指定了本entity为multipart，则不出现Content-Transfer-Encoding和Content-Disposition
                symbol_list = []
            elif current_node.symbol == "<parameter>":
                for key, value in current_node.parameter.items():
                    symbol_list.extend(["<semicolon>", "<space>", key, "<equal>", value])
            elif current_node.symbol == "<entity-body>":
                if multipart_entity_flag:
                    symbol_list = ["<multipart_body>"]
                    multipart_entity_flag = False
                else:
                    symbol_list = ["<individual_body>"]
            elif current_node.symbol == "<individual_body>":
                entity_CTE = self.get_entity_CTE(current_node.entity_root)
                symbol_list = [self.grammar["encoding_content_map"][entity_CTE]]
            elif current_node.symbol == "<boundary>":
                if mode == 0:
                    symbol_list = [boundary_stack[-1]]
                elif mode == 1:
                    symbol_list = [random.choice(self.grammar["<boundary>"])]         # 变异模式下 随机取了一个boundary #####
            elif current_node.symbol == "<id_str>":
                id_str = re.sub(r'.*?-', "", current_node.id)
                symbol_list = [id_str]
            else:
                # 可以自由选择扩展结果的情况
                symbol_list = self.get_expansion_result(current_node)

                if current_node.symbol == "<multipart_body>":
                    # 这里的赋值在构造中暂时没有实际用到 不过作为multipart body的必要属性记录下来
                    current_node.multipart_attr["is_multipart"] = True
                    if mode == 0:
                        current_node.multipart_attr["boundary"] = boundary_stack[-1]  # 直接取栈顶元素，即最近入栈的一个boundary
                    elif mode == 1:
                        current_node.multipart_attr["boundary"] = random.choice(self.grammar["<boundary>"])         # 变异模式下 随机取了一个boundary #####
                if current_node.symbol == "<multipart_begin_dash-boundary>":
                    nesting_depth += 1
                if current_node.symbol == "<multipart_end_dash>":
                    # 到达了一个multipart的结束 该multipart的boundary废止使用
                    if len(boundary_stack) > 0:             # is 0: 变异时新增<multipart_end_dash> #####
                        boundary_stack.pop()
                        nesting_depth -= 1

            # (2) 根据所选的扩展方式 逐个生成子节点并加入队列
            nonterminal_children = deque()
            for symbol in symbol_list:

                if len(symbol) == 0:
                    continue

                # For Debug
                if symbol == "<encapsulation>":
                    debug_mode = True

                new_node = Node(symbol, current_node)
                if symbol in self.grammar["entity-root"]:
                    new_node.entity_root = new_node
                else:
                    new_node.entity_root = current_node.entity_root

                if symbol == "<multipart>":
                    # boundary = hf.random_choose_with_weights(self.grammar["<boundary>"])
                    boundary = ("+++boundary_" + re.sub(r'<(.*?)>', "\g<1>", new_node.id) + "_boundary+++")
                    new_node.boundary_para = boundary
                    para_node = hf.get_node_by_symbol(node_queue, "<parameter>")
                    if para_node is not None:               # is None: 变异时新增c_type_subtype 且选择到multipart #####
                        para_node.parameter["boundary"] = boundary
                        multipart_entity_flag = True        # 目前队列里可能是mail-body 可能是entity-body
                        boundary_stack.append(boundary)     # 选择通过标志位+栈顶元素的方式为接下来的entity-body作出指示
                        self.add_grammar("<boundary>", boundary)
                elif symbol == "attachment":
                    filename = re.sub(r'.*?-', "att_", new_node.id)
                    new_node.filename_para = filename
                    para_node = hf.get_node_by_symbol(node_queue, "<parameter>")
                    if para_node is not None:
                        para_node.parameter["filename"] = filename
                    entity_CTE = self.get_entity_CTE(current_node.entity_root)
                    self.att_list.append(entity_CTE)

                current_node.children.append(new_node)

                if not new_node.is_terminal:
                    nonterminal_children.appendleft(new_node)
                    # node_queue.appendleft(new_node)
                    self.nonterminal_node_list[new_node.id] = new_node
            node_queue.extend(nonterminal_children)     # 保证DFS扩展顺序

        return start_node

    def get_expansion_result(self, node, exclusion=[]):
        possible_expansions = copy.copy(self.grammar[node.symbol])
        for excls in exclusion:
            possible_expansions.remove(excls)
        chosen_expansion = hf.random_choose_with_weights(possible_expansions)
        return re.split(Node.RE_NONTERMINAL, chosen_expansion)

    def add_grammar(self, key, value):
        if key in self.grammar.keys():
            self.grammar[key].append(value)
        else:
            self.grammar[key] = [value]

    def remove_subtree_from_nodelist(self, start_node):
        """ This function updates the node_list dictionary
            when a node (and as a result its children) are removed.
        """
        if not start_node.is_terminal:
            self.nonterminal_node_list.pop(start_node.id)
            for child in start_node.children:
                self.remove_subtree_from_nodelist(child)

    def tree_to_msg(self, partial=False):
        self.msg = b""
        self.expand_node(self.root)
        if partial:     # msg in its most basic form -- with placeholder values.
            return self.msg

        return self.msg

    def expand_node(self, node):
        if node.is_terminal:
            self.msg += node.symbol.encode('utf-8')
            # if isinstance(node.symbol, str):
            #     a = 1
            # self.request += node.symbol
        else:
            for child in node.children:
                self.expand_node(child)

    def search_node_in_entity(self, entity_root: Node, symbol):
        """
        在本实体对应的子树中查找节点
        :param entity_root:
        :param symbol:
        :return:
        """
        if entity_root.symbol == symbol:
            return entity_root

        res = None
        found_flag = False
        for child in entity_root.children:
            res = self.search_node_in_entity(child, symbol)
            if res is not None:
                found_flag = True
                break

        if found_flag:
            return res
        else:
            return None

    def get_entity_CTE(self, entity_root):
        entity_CTE_node = self.search_node_in_entity(entity_root, "<CTE>")
        if entity_CTE_node is None:
            return "7bit"
        else:
            return entity_CTE_node.children[0].symbol
