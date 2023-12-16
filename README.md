<h1 align="center">
    <a href="https://github.com/urimeba/database/">
    <img src="./Static/img/bd.png">
    </a>
</h1>

<p align="center">
  <i align="center">"Unlocking DataBass Potential: Seamlessly Empowering Management & Support 🚀</i>
</p>

<h4 align="center">
  <a href="https://github.com/urimeba/database/deployments/uaqdatabass">
    <img src="https://img.shields.io/github/actions/workflow/status/amplication/amplication/ci.yml?branch=master&label=pipeline&style=flat-square" alt="continuous integration" style="height: 20px;">
  </a>
  <a href="https://github.com/urimeba/database/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/urimeba/database" alt="contributors" style="height: 20px;">
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/github/license/urimeba/database" alt="license" style="height: 20px;">
  </a>
</h4>

## Purpose

`DataBass` is a remote database management tool designed for students. It enables access to a personal database activated by the designated teacher from any internet-connected device, fostering an understanding and learning of the necessary tools for SQL management and administration.

The platform operates with roles for teachers, classes, and students, allowing a teacher to create different classes with various exercises. These exercises can be activated or deactivated, restricting student access accordingly. Upon submission, students receive immediate feedback and grading for their completed exercises.

Teachers can view student grades per exercise, regardless of their active status. Additionally, didactic materials are available for consultation during classes, aiding in revisiting concepts and addressing queries.

The platform allows teachers to autonomously create student user accounts by uploading a CSV file with a specific format, simplifying user management.

The SQL compiler, a pivotal component, connects to a cloud-based database to execute SQL instructions created by students. Results obtained are evaluated against criteria set by the teacher, promoting practical and effective learning of SQL.

## Usage 
#### Step 1: Create a Virtual Environment
- **Unix/Linux/macOS Users:**
  ```bash
  python3 -m venv env
  ```
- **Windows Users:**
  ```bash
  py -m venv env
  ```

#### Step 2: Activate the Virtual Environment
- **Unix/Linux/macOS Users:**
  ```bash
  source env/bin/activate
  ```
- **Windows Users:**
  ```bash
  .\env\Scripts\activate
  ```

#### Clone the GitHub Repository
1. Run the following command in the terminal or Git Bash:
   ```bash
   git clone "https://github.com/urimeba/database"
   ```

#### Deploy Django Project from GitHub
1. Once the repository is successfully cloned, navigate to the cloned repository directory where the Django project is located.
2. If there's a `requirements.txt` file, install the project dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Django server:
   ```bash
   python manage.py runserver
   ```
   
#### Verify Application Deployment
1. Open a web browser and enter `http://127.0.0.1:8000` to verify if the application is running correctly.

## Development

Alternatively, Databass can be run locally for code generation purposes or contributions - if so, please refer to our [contributing](#contributing_anchor) section.


<details open>
<summary>
Pre-requisites
</summary> <br />
To be able to start development, make sure that you have the following prerequisites installed:

### Local Internet Connection
Ensure you have access to a local internet connection.

### Prerequisites
- **Django Framework Installed:** Make sure you have Django installed.
- **SQLiteStudio or Equivalent Database Manager supporting SQLite3:** Install SQLiteStudio or any other database manager that supports SQLite3.
- **Visual Studio Code:** Have Visual Studio Code installed for development purposes.
- **Web Browser:** Use Google Chrome, Mozilla Firefox, or any other browser that supports development purposes.

These prerequisites are necessary to proceed with setting up and developing within the Django environment.

</details>

<a name="contributing_anchor"></a>
## Contributing

Databass is an open-source project. We are committed to a fully transparent development process and highly appreciate any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as a part of the Databass community.

- Bug Report: If you see an error message or encounter an issue while using Databass, please create a [bug report](https://github.com/urimeba/database/issues/new?assignees=&labels=type%3A+bug&template=bug.yaml&title=%F0%9F%90%9B+Bug+Report%3A+).

- Feature Request: If you have an idea or if there is a capability that is missing and would make development easier and more robust, please submit a [feature request](https://github.com/urimeba/database/issues/new?assignees=&labels=type%3A+feature+request&template=feature.yml).

- Documentation Request: If you're reading the Databass docs and feel like you're missing something, please submit a [documentation request](https://github.com/urimeba/database/issues/new?assignees=&labels=type%3A+docs&template=documentation-request.yaml&title=%F0%9F%93%96+Documentation%3A+).

## Contributors

<!---
npx contributor-faces --exclude "*bot*" --limit 70 --repo "https://github.com/amplication/amplication"

change the height and width for each of the contributors from 80 to 50.
--->

[//]: contributor-faces

<a href="https://github.com/urimeba"><img src="https://avatars.githubusercontent.com/u/48847517?v=4" title="urimeba" width="50" height="50"></a>
<a href="https://github.com/Carlos5anchez"><img src="https://avatars.githubusercontent.com/u/43074684?v=4" title="Carlos5anchez" width="50" height="50"></a>
<a href="https://github.com/RichieSan"><img src="https://avatars.githubusercontent.com/u/43075160?v=4" title="RichieSan" width="50" height="50"></a>
<a href="https://github.com/Angel877898"><img src="https://avatars.githubusercontent.com/u/50708206?v=4" title="Angel877898" width="50" height="50"></a>
<a href="https://github.com/EladioRocha"><img src="https://avatars.githubusercontent.com/u/39393035?v=4" title="EladioRocha" width="50" height="50"></a>
<a href="https://github.com/Alexisdelrio392"><img src="https://avatars.githubusercontent.com/u/63680138?v=4" title="Alexisdelrio392" width="50" height="50"></a>

[//]: contributor-faces

## License
Our project is licensed under the Apache License 2.0. The Apache 2.0 license is a permissive open-source license that allows you to use, modify, distribute, and sublicense the project's code and any modifications you make. 

#### Key Points:
- **Permissions:** You have the freedom to use, copy, modify, merge, publish, distribute, sublicense, and sell the software.
- **Conditions:** Contributions and distributions must include the original license and any copyright notices.
- **Disclaimers:** The software is provided "as is," without warranties or conditions of any kind.

For detailed information, please refer to the [LICENSE](./LICENSE) file in this repository.

We encourage contributions from the community to help improve and grow this project!