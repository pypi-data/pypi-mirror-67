# test

1. generate a [Twine API token](https://pypi.org/help/#apitoken) in your account
   settings at [pypi](https://pypi.org/manage/account/)

2. Add the API key as an encrypted secret to your github repo:
   1. On GitHub, navigate to the main page of the repository.
   2. Under your repository name, click **Settings**.
   3. In the left sidebar, click **Secrets**.
   4. Type "`TWINE_API_KEY`" in the "Name" input box.
   5. Enter your twine API token.
   6. Click **Add secret**.

3. In `.github/workflows/pythonpublish.yml`, under the `Build and Publish` step,
   enter:

    ```yaml
    env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.TWINE_API_KEY }}
    ```
