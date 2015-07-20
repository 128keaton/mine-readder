**Official Thread:** [http://www.spigotmc.org/resources/mc-status-viewer.518/](http://www.spigotmc.org/resources/mc-status-viewer.518/)

**Installation:**

*   `git clone [https://github.com/vemacs/mc-status-viewer.git](https://github.com/vemacs/mc-status-viewer.git)` (I prefer in `/srv`)
*   Edit `index.html` to have the title you want
*   Edit `app/config.yml` to set up your categories and servers, see `[config.example.yml](https://github.com/vemacs/mc-status-viewer/blob/master/app/config.example.yml)`
*   `pip install bottle pyyaml`, depending on your distro, you may need to install `python-pip` and `python-dev` first
*   `cd <where you cloned>/app; python app.py`
*   You can test it by changing `app/app.py `to bind to `0.0.0.0 `and then connecting to `<ip>:8080`, `config.yml` is not accessible to the public, so your backends will stay hidden
*   Run it in a `tmux `or `screen` session
*   Set up a reverse proxy, here&#039;s a [sample nginx config](http://paste.ubuntu.com/7301975/), [Apache instructions](http://paste.ubuntu.com/7401472/)
*   `git pull` to update if there are any updates
*   You can **change the width** by editing `override.css` in the` .btn` class if you have longer server names

Post feedback or suggestions here! Keep in mind that I'm a noob at Python and Javascript (I literally learned JS today), so any code quality feedback would be awesome.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
