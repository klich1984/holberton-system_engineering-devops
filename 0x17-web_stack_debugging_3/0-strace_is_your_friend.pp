# Find out why Apache is returning a 500 error with strace
exec { 'debugging':
    provider => 'shell',
    command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
