# create file /tmp/holberton:

file { 'create /tmp/holberton' :
  ensure  => 'present',
  path    => '/tmp/holberton',
  mode    => 'u+rwx',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
