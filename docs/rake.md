# Rake Tasks

If you have Ruby installed on your system (*if you are on macOS you’ll have it by default*)
you can easily automate your basic operations. Run `rake -T` for listing
available tasks:

```bash
$ rake -T

rake db:migrate[database]                                        # Run migration for given database (default: 'default')
rake db:roll_back[name_of_application,name_of_migration]         # Roll-back (name of application, name of migration)
rake db:shell                                                    # run database shell ..
rake db:show[name_of_application]                                # Show migrations for an application (default: 'all')
rake db:update[name_of_application,name_of_migration,is_empty]   # Update migration (name of application, name of migration?, is empty?)
rake default                                                     # Default task: runserver_plus (Werkzeug)
rake locale:compile                                              # Compile locale dictionary
rake locale:update                                               # Update locale dictionary
rake new:application[name_of_application]                        # Create new Django application
rake new:model[name_of_application,name_of_model,type_of_model]  # Create new Model for given application: django,basemodel,softdelete
rake runserver:default                                           # Run: runserver (Django's default server)
rake runserver:default_ipdb                                      # Run: runserver (Django's default server) + ipdb debug support
rake runserver:plus                                              # Run: runserver_plus (Werkzeug)
rake runserver:plus_ipdb                                         # Run: runserver_plus (Werkzeug) + ipdb debug support
rake shell[repl]                                                 # Run shell+ avail: ptpython,ipython,bpython default: ptpython
rake test:browse_coverage[port]                                  # Browse test coverage
rake test:coverage[cli_args]                                     # Show test coverage (default: '--show-missing --ignore-errors --skip-covered')
rake test:run[name_of_application,verbose]                       # Run tests for given application
```

Rake tasks are the wrapper for Django’s management commands. Mostly related
to `django-vb-baseapp` application. Please checkout https://github.com/vbyazilim/django-vb-baseapp
for more detail and examples. `django-vb-baseapp` has lot of features :)
