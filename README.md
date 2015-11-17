## Drupal Analysis Tools

Analyze a Drupal website from the position of an adversary.

Only run on authorized sites.

### Install Dependencies

```pip install -r REQUIREMENTS.txt```

### Scripts

```common.users_from_node(base_url)``` : returns a list of usernames from a Drupal site by analyzing the nodes.  These are only the publically visible usernames that have posted.


### Quick run

Uncomment the sample at the bottom of ```common.py```, replace string with your own address, and run common.py: ```python common.py```
