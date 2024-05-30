# Flowstate University 
## Project Handoff

This repository contains the file structure and instructions for styling the currently enabled 'flowstate' Tutor
theme, instructions for maintaining the wiki, and documentation on the MFE (micro front end) styling process.

- [Theming](#open-edx-theming)
- [Wiki](#wiki)
- [Micro Front End](#micro-front-end-plugin)

### Useful Links

1. [Tutor Documentation](https://docs.tutor.overhang.io/)
2. [Open EdX Theming Documentation](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/ecommerce/theming.html)
3. [Open EdX Github Repository](https://github.com/openedx/edx-platform)

 
# Open Edx Theming

Styling sections of Open Edx is done via custom themes. The 'flowstate' directory in this repo mirrors the content in the existing 'flowstate' theme, currently running.

## Files:
### Assets:
/cms/static/images/ - Flowstate favicon and studio logo for cms (studio)

/lms/static/fonts/ - Flowstate fonts

/lms/static/images/ - lms (university) standard images and flowstate favicon, banner, footer 

### Styling:
/lms/static/sass/partials/lms/theme/_fonts.scss - sets default fonts for theme

/lms/static/sass/partials/lms/theme/_variables.scss - sets default variables (font and color)

/lms/static/sass/* - specific styling for sections (courseware, dashboard, footer, header, home)

### Html templates:
/lms/templates/footer.html - Flowstate footer logo, TOS and Copyright info

/lms/templates/header/navbar-authenticated.html - link to wiki (currently commented out)

## Building the Open Edx Theme

From within open edx instance:
1. replace/edit flowstate theme files via scp or nano
   - ``scp -r flowstate FlowUser@137.117.127.150:~/.local/share/tutor/env/build/openedx/themes/`` for full directory
   - nano (command line text editor) has been installed. (note - any changes made to the 'live' files should be copied into this repo if you intend to use scp)
2. shut down openedx - `tutor local stop`
3. Run the theme build command and restart commands: `tutor images build openedx && tutor local start -d`
   - Initial builds can take some time. If the system freezes, see Nick to restart VM. 
4. Only necessary if creating new theme or switching to a different theme:  `tutor local do set theme flowstate`

[Back to top](#project-handoff)

# Wiki

 - The Wiki is located at https://university.flowstate.support/wiki/

 - Enabling the link in navbar-authenticated.html by uncommenting will place the "Wiki" link next to "Courses" 

 - The majority of the content from zendesk has been transferred, but some text and images still need moved. 

 - The images linked have been uploaded into the "Flowstate LDS Basic User Training" Files & Uploads. 

 - The wiki uses standard markdown, but the majority of HTML styling is stripped out - namely tables and highlighting, which are used extensively in the zendesk version. 
Work with Angie on the best way to get around this. suggestion for tables - Create them elsewhere and im port as image?  

[Back to top](#project-handoff)

# Micro Front End Plugin

For certain sections (including '/learning' where course content resides), Tutor Open Edx has moved from the legacy comprehensive theming used above to a plugin system.
It's convoluted and I have been unable to get it to work as intended - but here are the steps taken and some additional resources:

1. Clone and edit brand repository Example:  https://github.com/stevenspicher/brand-openedx.git (changes fonts and default colors)
2. Create plugin file in ~.local/share/tutor-plugins (this instructs the build to install repo)

   Example plugin format, saved as 'mfe_brand.py':
      ```
      from tutor import hooks
   
      hooks.Filters.ENV_PATCHES.add_item(
      (
      "mfe-dockerfile-post-npm-install",
      """
      # git repository
      RUN npm install '@edx/brand@git+https://github.com/stevenspicher/brand-openedx.git'
      """
      )
      )
      ```
2. Shut down openedx - `tutor local stop` 
3. Enable plugin
   - show plugins list (plugins will show installed/enables status) - `tutor plugins list`
   - enable plugin - `tutor plugins enable mfe_brand.py`
   - save changes - `tutor config save`
   - build micro front end - `tutor images build mfe` 
     - If build freezes, try appending `--no-cache --no-registry-cache`
     - the install log _should_ show the repo installation (it scrolls as build is running)  
4. Restart Open Edx - `tutor local start -d`

Documentation for plugins/mfe:

- [Tutor Plugin Documentation](https://docs.tutor.edly.io/tutorials/plugin.html)
- [Tutor MFE](https://github.com/overhangio/tutor-mfe)








[Back to top](#project-handoff)