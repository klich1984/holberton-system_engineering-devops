#  create a manifest that kills a process named killmenow Ussing puppet
exec { 'task2':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
