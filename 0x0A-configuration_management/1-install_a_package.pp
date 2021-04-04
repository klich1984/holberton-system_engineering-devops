# Install puppet-lint using puppet
package { 'task-1':
  name    => 'puppet-lint',
  ensure  => '2.1.1',
  provider => 'pip3'
}
