# install server nginx

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx install':
  ensure  => latest,
  require => Exec['apt-get update']
}

exec { 'nginx start':
  command  => 'etc/init.d/nginx start',
  required => Exec['nginx install']
}

exec { 'new html':
  command  => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html',
  required => Exec['nginx start']
}

exec { 'redirection':
  command  => 'sed -i \'s|_;|_;\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGlwu4 permanent;|g\' /etc/nginx/sites-available/default',
  required => Exec['new html']
}
