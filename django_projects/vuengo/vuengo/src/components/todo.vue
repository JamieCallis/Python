<template>
  <div class="hello">
    <h1 class="title">Vuengo</h1> <!-- Page title -->

    <hr>

    <div class="columns">
    <div class="column is-one-third is-offset-one-third">
      <form v-on:submit.prevent="addTask"> <!-- v-on:submit.prevent="addTask" calls the function addTask on submit -->
        <h2 class="subtitle">Add task</h2>

        <div class="field">
          <label class="label">Description</label>
          <div class="control">
            <input class="input" type="text" v-model="description"> <!-- Connects this field to the description variable -->
          </div>
        </div>

        <div class="field">
          <label class="label">Status</label>
          <div class="control">
            <div class="select">
              <select v-model="status"> <!-- Connects this field to the status variable -->v
                <option value="0">To do</option>
                <option value="1">Done</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Submit</button>
          </div>
        </div>
      </form>
    </div>
  </div>

    <hr>

    <div class="columns">
        <div class="column is-half">
          <h2 class="subtitle">Todo</h2>

          <div class="todo">
            <div class="card" v-for="(task, index) in filtertasks(0)" v-bind:key="index"> <!-- Loop through the tasks array, if status is 0 (to do) then we'll show it. -->
              <div class="card-content">
                <div class="content">
                  {{ task.description }} <!-- Print the task's description here -->
                </div>
              </div>

              <footer class="card-footer">
                <a class="card-footer-item" v-on:click="setStatus(task.id)">Done</a>
              </footer>
            </div>
          </div>
        </div>

        <div class="column is-half">
          <h2 class="subtitle">Done</h2>

          <div class="done">
            <div class="card" v-for="(task, index) in filtertasks(1)" v-bind:key="index" > <!-- Loop through the tasks array, if status is 1 (done) then we'll show it. -->
              <div class="card-content">
                <div class="content">
                  {{ task.description }}
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'todo',
  data () {
    return {
      tasks: [], // Array for holding the tasks
      description:'',
      status: 0
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getTasks(); // Call our getTasks function below
  },
 
  methods: {
    filtertasks(option) {
      var filterdone = []
      this.tasks.filter(function(item) {
        if(item.status == option) {
          filterdone.push(item)
        }
      })

      return filterdone
    },
    getTasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/tasks/',
            auth: {
                username: 'jamie',
                password: 'password'
            }
        }).then(response => this.tasks = response.data);
    },

    addTask() {
      if(this.description) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/tasks/',
          data: {
            description: this.description,
            status: this.status
          },
          auth: {
            username: 'jamie',
            password: 'password'
          }
        }).then((response) => {
          let newTask = {'id': response.data.id, 'description': this.description, 'status': parseInt(this.status)}

          this.tasks.push(newTask)

          this.description = '' // reset description
          this.status = 0 // reset status
          getTasks()
        }).catch((error) => {
          console.log(error);
        });
      }
    },

    setStatus(task_id) {
      let description = '';

      for (let task = 0; task < this.tasks.length; task++) {
        if (this.tasks[task].id === task_id) {
          this.tasks[task].status = 1
          description = this.task[task].description

          break
        }
      }

      axios({
        method:'put',
        url: 'http://127.0.0.1:8000/tasks/' + task_id + '/',
        header: {
          'Content-Type': 'application/json'
        },
        data: {
          description: description,
          status: 1
        },
        auth: {
          username: 'admin',
          password: 'Golden77871838'
        }
      })
    }
  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
