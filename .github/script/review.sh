  
  curl \
  -X POST \
  -H "authorization: Bearer $GH_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/pulls/"$PR_NUMBER"/comments/572382525/replies \
  -d '{"body":"Your review comment does not follow review etiquette"}'


curl \
  -X PATCH \
  -H "authorization: Bearer $GH_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/pulls/comments/572382704 \
  -d '{"body":"adding reply"}'
  
curl \
  -X POST \
  -H "authorization: Bearer $GH_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/issues/56/comments\
  -d '{"body":"body"}'



echo "54"
