# nueroflow-project


My Notes:
Used Flask documentation and tutorial on Python 3.
Basic api created from what knowledge I learned from the internet, since I haven't reached this level in my university. 
Using Flask, the api use the mood class to create the mood endpoint and creates the get and post methods.
The login purposes have been created using the Flask request import utilizing the authentication methods.
Unable to correctly approach streak problem and count not develope solution. 
I think moving forward to larger scale would require a sql server database and a more generalized api that the one I attempted to create.

Requirements:

Create a web REST application with a '/mood' endpoint, which when POSTed to persists the submitted mood value.

Add the ability for users to login.

Update the '/mood' endpoint with a GET method, so it only returns values submitted by the logged-in user.

Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".
●	A user is on a “streak” if that user has submitted at least 1 mood rating for each consecutive day of that streak.
For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered mood ratings, a 3-day streak will apply to the March 3rd rating and the streak will reset to a 1-day streak for the March 5th rating.

Document what, if anything, you would do differently if this were a production application and not an assessment? What tech would you use? How would you handle things differently if it needed to handle more users, more data, etc?
