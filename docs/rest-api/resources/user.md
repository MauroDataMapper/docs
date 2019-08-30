<endpoint class="get">/api/catalogueUsers</endpoint>
<endpoint class="post">/api/catalogueUsers</endpoint>
<endpoint class="get">/api/catalogueUsers/**{id}**</endpoint>
<endpoint class="put">/api/catalogueUsers/**{id}**</endpoint>
<endpoint class="delete">/api/catalogueUsers/**{id}**</endpoint>



## Admin functionality

<endpoint class="post">/api/catalogueUsers/adminRegister</endpoint>
<endpoint class="get">/api/catalogueUsers/pending</endpoint>
<endpoint class="get">/api/catalogueUsers/userExists/**{emailAddress}**</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/adminPasswordReset</endpoint>
<endpoint class="get">/api/catalogueUsers/**{catalogueUserId}**/resetPasswordLink</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/rejectRegistration</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/approveRegistration</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/changePassword</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/userPreferences</endpoint>
<endpoint class="get">/api/catalogueUsers/**{catalogueUserId}**/userPreferences</endpoint>


## Search

<endpoint class="get">/api/catalogueUsers/search/**{searchTerm?}**</endpoint>
<endpoint class="post">/api/catalogueUsers/search</endpoint>
 
 

## Profile images


<endpoint class="get">/api/catalogueUsers/**{catalogueUserId}**/image</endpoint>
<endpoint class="post">/api/catalogueUsers/**{catalogueUserId}**/image</endpoint>
<endpoint class="put">/api/catalogueUsers/**{catalogueUserId}**/image</endpoint>
<endpoint class="delete">/api/catalogueUsers/**{catalogueUserId}**/image</endpoint>
