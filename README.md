This application utilizes Django Framework ... It works on Python >= 3.5

Install Django:
```
Anaconda users:
$  conda install -c anaconda django 
Otherwwise:
$ pip install Django==2.1
```

Install Dash-Plotly
```
pip install dash==0.24.1  # The core dash backend
pip install dash-renderer==0.13.0  # The dash front-end
pip install dash-html-components==0.11.0  # HTML components
pip install dash-core-components==0.27.1  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library used in examples

For Conda users:
conda install -c conda-forge dash-renderer
conda install -c conda-forge dash 
conda install -c conda-forge dash-html-components 
conda install -c conda-forge dash-core-components
conda install -c conda-forge plotly
```

Download this repository:
```
$ git clone https://github.com/ag3456/WebFrameworkTest.git
$ cd WebFrameworkTest/buscp
```

Start the server:
```
$ python manage.py runserver
```
Open browser and go to:
http://127.1.0.0:8000/gtfls 
