<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInited1211abd05247e76db5b3b5c169f7ce
{
    public static $prefixLengthsPsr4 = array (
        'E' => 
        array (
            'Eki\\Mimeminer\\' => 14,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Eki\\Mimeminer\\' => 
        array (
            0 => __DIR__ . '/../..' . '/src',
        ),
    );

    public static $prefixesPsr0 = array (
        'e' => 
        array (
            'eXorus\\PhpMimeMailParser\\' => 
            array (
                0 => __DIR__ . '/..' . '/php-mime-mail-parser/php-mime-mail-parser/src',
            ),
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInited1211abd05247e76db5b3b5c169f7ce::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInited1211abd05247e76db5b3b5c169f7ce::$prefixDirsPsr4;
            $loader->prefixesPsr0 = ComposerStaticInited1211abd05247e76db5b3b5c169f7ce::$prefixesPsr0;
            $loader->classMap = ComposerStaticInited1211abd05247e76db5b3b5c169f7ce::$classMap;

        }, null, ClassLoader::class);
    }
}