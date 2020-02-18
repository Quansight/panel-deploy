panel-deploy
-------

`panel-deploy` is a click-based cli for deploying panel applications.


### Install from Github
```bash
git clone https://github.com/Quansight/panel_deploy && cd panel_deploy && pip install -e .
```

### Add Usage Example Here

 panel-deploy --environment_file_path /your/application/environment.yml 
              --notebook_file_path  /your/application/notebook.ipynb
              --server_ip 192.167.56.54
              --notebook_name iris_kmeans.ipynb
              --conda_env_name panel iris_kmeans
              
### Options

```bash
panel-deploy --help

Usage: panel-deploy [OPTIONS]

Options:
  --environment_file_path TEXT
  --notebook_file_path TEXT
  --server_ip TEXT
  --notebook_name TEXT
  --conda_env_name TEXT
  --server_name TEXT
  --use_ssl TEXT
  --ssl_certificate TEXT
  --ssl_certificate_key TEXT
  --current_user TEXT
  --secret_key TEXT
  --user_password TEXT
```
