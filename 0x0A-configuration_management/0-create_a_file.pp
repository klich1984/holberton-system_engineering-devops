# create file in /tmp Using Puppet
file { 'task 0':
  ensure  => file,
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
}
