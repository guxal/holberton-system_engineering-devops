# create file /ssh_config:
$pth = '/etc/ssh/ssh_config'

file_line { 'authentication password no' :
  ensure => present,
  path   => $pth,
  line   => '    PasswordAuthentication no'
}

file_line { 'use private key holberton' :
  ensure => present,
  path   => $pth,
  line   => '    IdentityFile ~/.ssh/holberton'
}
