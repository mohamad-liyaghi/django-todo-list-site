## Introduction
<p>Django Todo list is a task manager website. This Project contains 5 apps.</p>
<ol>
    <li>Accounts</li>
    <li>Task</li>   
    <li>Routine</li>
    <li>Project</li>
    <li>Api</li>
</ol>

<hr>
<h3>Accounts</h3>
<p>This Project is using django-allauth package for authentication purposes. The user model and some basic views are stored in this app.</p>

<hr>
<h3>Task</h3>
<p>This app handles Add/Update/Delete Task. Users can add tasks, update the status and also delete them.</p>

<hr>
<h3>Routine</h3>
<p>This App works same as tasks app. They are some common views that are stored in both apps.</p>

<hr>
<h3>Project</h3>
<p>In this app users can create their own projects and then add tasks for that project.</p>


<hr>
<h3>Api</h3>
<p>They are 2 versions of Apis in this project.</p>
<p>V1 is the old one, its not recommended.</p>
<p>V2 is the latest api that is implemented. it is more secure and reliable. this version is using djoser for jwt authentication purposes. </p>



## How to use:

### clone the project:

```commandline
git clone https://github.com/mohamad-liyaghi/django-todo-list-site.git
```

### now run it via docker

```commandline
docker-compose up --build
```

Good Luck.
