# seattle200
1. User profile and repository data were gathered through paginated API requests to GitHub, using authorization headers for secure access, in Pyhthon. Repositories were accessed via each user’s repository endpoint, with pagination ensuring up to 500 repositories were retrieved while managing rate limits with strategic pauses.
2. Having a wiki appears to be beneficial for repository engagement, as repositories with a wiki (regardless of having projects or not) have higher average stars than those without. What was surprising is, repositories with both projects and wikis show unexpectedly lower average stars, suggesting that heavily structured repositories may attract less popularity or reflect a selection bias.
Based on above insight, developers should prioritize a comprehensive wiki with clear documentation to enhance repository appeal and foster greater user interaction and stars.
