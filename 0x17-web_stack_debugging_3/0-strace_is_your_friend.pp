# fix the apache2 wordpress

exec { 'sed':
  command => '/bin/sed -i \'s|phpp|php|g\' /var/www/html/wp-settings.php'
}
