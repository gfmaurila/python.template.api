from infrastructure.repositories.GithubMongoRepository import GithubMongoRepository
from bson import ObjectId

class GetStoredUserProfileQuery:
    def __init__(self):
        self._repository = GithubMongoRepository()

    def Handle(self) -> dict | None:
        profile = self._repository.GetStoredUserProfile()
        if profile and "_id" in profile:
            profile["_id"] = str(profile["_id"])  # <- convertendo o ObjectId para string
        return profile
