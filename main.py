
from uwureddit.uwureddit import uwureddit

uwu = uwureddit(
    "wcwdqCBWul9HyU4y0iPgvA",
    "JWKc5XX2nAuv8SLpUE4uwQtEVpRH-Q"
)

sub = uwu.subreddit("AnimeART")
print(sub.user_is_subscriber)
