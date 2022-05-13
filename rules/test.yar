rule test
{
    strings:
        $a = "cmd" nocase
    condition:
        $a
}