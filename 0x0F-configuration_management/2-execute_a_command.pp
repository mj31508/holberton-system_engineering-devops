# killing a process with python

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',

}
