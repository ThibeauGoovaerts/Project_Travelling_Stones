import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web_rest_api.settings")
django.setup()

from travelling_stones import models  # noqa: E402

personne = models.Personne.objects.get(username="maintenance")
if personne.hashtag == "true":
    personne.hashtag = "false"
else:
    personne.hashtag = "true"

personne.save()
