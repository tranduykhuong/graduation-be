# This is base Django project

## File structure

```
.
|
├── app
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
|   └── settings
│         └── cache.py
├── app_core
│   ├── apps.py
│   ├── exceptions.py
│   ├── models.py
│   ├── renderers.py
│   ├── responses.py
│   └── routes.py
├── app_example
│   ├── migrations
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── tests.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
└── ...
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

## Run Locally

This project uses Python 3.11 version

Go to the project directory

Install dependencies

```bash
  pip install -r requirements.txt
```

Migration

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

## Branching Strategy:

1. **Develop Branch (Staging):**
   - The `develop` branch is designated for staging deployments.
   - All feature branches should be merged into `develop` for testing and staging purposes.
   - Developers are encouraged to create feature branches from `develop`.

2. **Main Branch (Production):**
   - The `main` branch is reserved for production deployments.
   - Only thoroughly tested and approved changes from the `develop` branch should be merged into `main`.
   - It is crucial to ensure that only stable and production-ready code is pushed to the `main` branch.

## Deployment Process:

### Staging Deployment:

1. **Feature Development:**
   - Developers should create feature branches from the latest commit in the `develop` branch.

2. **Code Review:**
   - All changes must go through a code review process before being merged into the `develop` branch.

3. **Merge to Develop:**
   - Once the feature is approved and the code review is completed, the changes should be merged into the `develop` branch.

4. **Staging Testing:**
   - Deploy the `develop` branch to the staging environment for thorough testing.

5. **Bug Fixing:**
   - If issues are identified during staging testing, they should be addressed on feature branches and merged back into `develop`.

6. **Approval for Production:**
   - After successful testing and bug fixing, obtain approval from the relevant stakeholders for production deployment.

### Production Deployment:

1. **Merge to Main:**
   - Only approved changes from the `develop` branch should be merged into the `main` branch for production.

2. **Monitoring:**
   - Monitor the production environment closely for any unexpected issues.
   - Rollback procedures should be in place in case of critical problems.

3. **Communication:**
   - Communicate the successful production deployment to the team and stakeholders.

*By following these guidelines, you establish a clear separation between staging and production environments, ensuring that only thoroughly tested and approved changes are deployed to production.*

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [REST Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Support

For support, email tranduykhuongit@gmail.com for supports.
