
Example for how to use Flask: 
    routes, WTForms, "flash" messages, and macros.


== Installation

<pre>
mkdir ~/git
git clone github.com/indera/flask-simple-form

sudo pip install virtualenv
sudo pip install virtualenvwrapper
sudo pip install fabric

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/git
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv -p /usr/local/bin/python2.7 flask-simple-form
workon flask-simple-form
cd ~/git/flask-simple-form
pip install -r requirements.txt

./run

open -a "Google Chrome.app" "http://localhost:5002"
</pre>
