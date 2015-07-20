**See it in action:** [BeardCraft Subreddit](http://reddit.com/r/beardcraftmc)

**Installation (For Status Page):**

*   Deploy to Heroku
*   Edit `index.html` to have the title you want
*   Edit `app/config.yml` to set up your categories and servers, see `[config.example.yml](https://github.com/vemacs/mc-status-viewer/blob/master/app/config.example.yml)`
*   You can **change the width** by editing `override.css` in the` .btn` class if you have longer server names
*   Visit `http://your-app-name-here.heroku.com` to see your awesomeness.
*

**Installation (For Subreddit Updater):**
* Create a wiki page called 'edit_sidebar' (you can do this by just typing reddit.com/r/YOURSUBHERE/wiki/edit_sidebar then clicking on: Create Page "edit_sidebar")
* Copy and paste the current sidebar that you have into the wiki page (The entire sidebar)
* Where you want the player count to go, type `***` then hit enter twice and type `***`
* Make sure there are no other lines of `***` anywhere else in the sidebar or things will get really messed up
* Save the wiki page
* Edit app.py to include yours subreddit name (without the /r/) and your bot's username and password.
* 
**To-Do**
* Make it easier to configure stuff.
* Make python query faster.



[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
