# execute 'apt-get update'
exec { 'apt-update':                    # exec resource named 'apt-update'
  command => '/usr/bin/apt-get update', # command this resource will run
}

# install nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],        # require 'apt-update' before installing
}

# ensure nginx service is running
service { 'nginx':
  ensure  => running,
}

# create directory if not exists
exec { 'create-directory':
  command => '/bin/mkdir -p /var/www/html/',
  require => Package['nginx']           # require 'nginx' package before creating
}

# ensure index file exists
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',        # index file
  require => Exec['create-directory'],  # require directory for storage
}

# add redirect_me rewrite in site_available
exec { 'redirect':
  command => '/bin/sed -i \'s|_;|_;\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGlwu4 permanent;|g\' /etc/nginx/sites-available/default',
  require => Package['nginx']
}
