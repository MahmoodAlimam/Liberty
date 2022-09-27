# Liberty

### POST `http://localhost:8000/api/v1/login`

User login route.\
return access_token and status success also set cookies of refresh_token, access_token and logged_in

### POST `http://localhost:8000/api/v1/register`

User register route.\
different user field and relationship as required. 

### POST `http://localhost:8000/api/v1/forget/password`

User forget password route.\
send email in which user want to get email link of forget password

### GET `http://localhost:8000/api/v1/user`

User route.\
get current logged in user by sending JWT in headers.

### GET `http://localhost:8000/api/v1/refresh`

Refresh access token route.\
get refreshed access token from refresh token which expiry is more 

### POST `http://localhost:8000/api/v1/file/upload`

Upload file route.\
upload file like photos videos audios etc also user profile picture also we can use S3 AWS service for this

### GET `http://localhost:8000/api/v1/file/{filename}`

Get file with unique filename.\
get file whiich you want from this route.

### GET `http://localhost:8000/api/v1/tokens`

Get all user token.\
get all users token.

### GET `http://localhost:8000/api/v1/nfts`

Get all nfts of user or limited.\
get NFTS of user its limited or all managed by Query params or different ways

### GET `http://localhost:8000/api/v1/collections`

Get all collections of user.\
Get all collection of users with pagination

### POST `http://localhost:8000/api/v1/collections`

Create a new collection by user.\
create a new collection of user.

### GET `http://localhost:8000/api/v1/collections/{id}`

Get single collection.\
get any single collection of user

### PUT `http://localhost:8000/api/v1/collections/{id}`

Update any collection.\
update any NFT collection of currently logged in user

### DELETE `http://localhost:8000/api/v1/collections/{id}`

Delete any collection.\
delete any collection of currently logged in user

### POST `http://localhost:8000/api/v1/addtoken`

Add token.

### POST `http://localhost:8000/api/v1/addnft`

Add nft.

### POST `http://localhost:8000/api/v1/send`

Send any token.

### `http://localhost:8000/api/v1/market`

All market API which are required and as needed after working on this section

### `http://localhost:8000/api/v1/payment/gateway`

Payment Gateways ALl API'S.\
Payment gateway which are required to use. Different Payment API'S are required.\
As Per requirement
