follow the steps below:

1. `git add {FILES}` to add the changes to the staging area.
2. `git commit -m "{COMMIT_MESSAGE}"` to commit the changes.

- {FILES} is the list of files you created or modified just now, but not all changed files, separated by spaces
- {COMMIT_MESSAGE} should satisfy the following requirements:
  - use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
  - use [GitMoji](https://gitmoji.dev/)
  - a concise summary of the changes
  - a link to the task record in `.agent/tasks/{TASK_RECORD_FILE}` if there is one
  - a link to the reflection in `.agent/reflections/{REFLECTION_FILE}` if there is one

----

## Conventional Commits 1.0.0

The Conventional Commits specification is a lightweight convention on top of commit messages.
It provides an easy set of rules for creating an explicit commit history;
which makes it easier to write automated tools on top of.
This convention dovetails with [SemVer](http://semver.org/),
by describing the features, fixes, and breaking changes made in commit messages.

The commit message should be structured as follows:

```plaintext
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the
consumers of your library:

1. **fix:** a commit of the *type* `fix` patches a bug in your codebase (this correlates with [`PATCH`](http://semver.org/#summary) in Semantic Versioning).
2. **feat:** a commit of the *type* `feat` introduces a new feature to the codebase (this correlates with [`MINOR`](http://semver.org/#summary) in Semantic Versioning).
3. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:`, or appends a `!` after the type/scope, introduces a breaking API change (correlating with [`MAJOR`](http://semver.org/#summary) in Semantic Versioning).
   A BREAKING CHANGE can be part of commits of any *type*.
4. *types* other than `fix:` and `feat:` are allowed, for example [@commitlint/config-conventional](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional) (based on the [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)) recommends `build:`, `chore:`,
   `ci:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`, and others.
5. *footers* other than `BREAKING CHANGE: <description>` may be provided and follow a convention similar to
   [git trailer format](https://git-scm.com/docs/git-interpret-trailers).

Additional types are not mandated by the Conventional Commits specification, and have no implicit effect in Semantic Versioning (unless they include a BREAKING CHANGE).
A scope may be provided to a commit's type, to provide additional contextual information and is contained within parenthesis, e.g., `feat(parser): add ability to parse arrays`.

----

## GitMoji

GitMoji is an emoji guide for GitHub commit messages. Using emojis in commit messages provides an easy way to identify the purpose or intention of a commit with only looking at the emojis used.

Here's a list of emojis and their meanings:

- 🎨 `:art:` - Improve structure / format of the code.
- ⚡️ `:zap:` - Improve performance.
- 🔥 `:fire:` - Remove code or files.
- 🐛 `:bug:` - Fix a bug.
- 🚑 `:ambulance:` - Critical hotfix.
- ✨ `:sparkles:` - Introduce new features.
- 📝 `:memo:` - Add or update documentation.
- 🚀 `:rocket:` - Deploy stuff.
- 💄 `:lipstick:` - Add or update the UI and style files.
- 🎉 `:tada:` - Begin a project.
- ✅ `:white_check_mark:` - Add, update, or pass tests.
- 🔒 `:lock:` - Fix security or privacy issues.
- 🔐 `:closed_lock_with_key:` - Add or update secrets.
- 🔖 `:bookmark:` - Release / Version tags.
- 🚨 `:rotating_light:` - Fix compiler / linter warnings.
- 🚧 `:construction:` - Work in progress.
- 💚 `:green_heart:` - Fix CI Build.
- 🔽 `:arrow_down:` - Downgrade dependencies.
- 🔼 `:arrow_up:` - Upgrade dependencies.
- 📌 `:pushpin:` - Pin dependencies to specific versions.
- 👷 `:construction_worker:` - Add or update CI build system.
- 📈 `:chart_with_upwards_trend:` - Add or update analytics or track code.
- ♻️ `:recycle:` - Refactor code.
- ➕ `:heavy_plus_sign:` - Add a dependency.
- ➖ `:heavy_minus_sign:` - Remove a dependency.
- 🔧 `:wrench:` - Add or update configuration files.
- 🔨 `:hammer:` - Add or update development scripts.
- 🌐 `:globe_with_meridians:` - Internationalization and localization.
- ✏️ `:pencil2:` - Fix typos.
- 💩 `:poop:` - Write bad code that needs to be improved.
- ⏪ `:rewind:` - Revert changes.
- 🔀 `:twisted_rightwards_arrows:` - Merge branches.
- 📦 `:package:` - Add or update compiled files or packages.
- 👽 `:alien:` - Update code due to external API changes.
- 🚚 `:truck:` - Move or rename resources (e.g.: files, paths, routes).
- 📄 `:page_facing_up:` - Add or update license.
- 💥 `:boom:` - Introduce breaking changes.
- 🍱 `:bento:` - Add or update assets.
- ♿️ `:wheelchair:` - Improve accessibility.
- 💡 `:bulb:` - Add or update comments in source code.
- 🍻 `:beers:` - Write code drunkenly.
- 💬 `:speech_balloon:` - Add or update text and literals.
- 🗃️ `:card_file_box:` - Perform database related changes.
- 🔊 `:loud_sound:` - Add or update logs.
- 🔇 `:mute:` - Remove logs.
- 👥 `:busts_in_silhouette:` - Add or update contributor(s).
- 🚸 `:children_crossing:` - Improve user experience / usability.
- 🏗️ `:building_construction:` - Make architectural changes.
- 📱 `:iphone:` - Work on responsive design.
- 🤡 `:clown_face:` - Mock things.
- 🥚 `:egg:` - Add or update an easter egg.
- 🙈 `:see_no_evil:` - Add or update a .gitignore file.
- 📸 `:camera_flash:` - Add or update snapshots.
- ⚗️ `:alembic:` - Perform experiments.
- 🔍 `:mag:` - Improve SEO.
- 🏷️ `:label:` - Add or update types.
- 🌱 `:seedling:` - Add or update seed files.
- 🚩 `:triangular_flag_on_post:` - Add, update, or remove feature flags.
- 🥅 `:goal_net:` - Catch errors.
- 💫 `:dizzy:` - Add or update animations and transitions.
- 🗑️ `:wastebasket:` - Deprecate code that needs to be cleaned up.
- 🛂 `:passport_control:` - Work on code related to authorization, roles and permissions.
- 🩹 `:adhesive_bandage:` - Simple fix for a non-critical issue.
- 🧐 `:monocle_face:` - Data exploration/inspection.
- ⚰️ `:coffin:` - Remove dead code.
- 🧪 `:test_tube:` - Add a failing test.
- 👔 `:necktie:` - Add or update business logic.
- 🩺 `:stethoscope:` - Add or update healthcheck.
- 🧱 `:bricks:` - Infrastructure related changes.
- 🧑‍💻 `:technologist:` - Improve developer experience.
- 💸 `:money_with_wings:` - Add sponsorships or money related infrastructure.
- 🧵 `:thread:` - Add or update code related to multithreading or concurrency.
- 🦺 `:safety_vest:` - Add or update code related to validation.
- ✈️ `:airplane:` - Improve offline support.
