curl \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/pulls/"$PR_NUMBER"/comments
  
  
  curl \
  -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/pulls/"$PR_NUMBER"/comments/572382525/replies \
  -d '{"body":"Your review comment does not follow review etiquette"}'


curl \
  -X PATCH \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/deepeshp656/TestLabel/pulls/comments/572382704 \
  -d '{"body":"adding reply"}'



echo "54"
