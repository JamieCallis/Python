<template>
  <div class="home">
    <!-- Sends the information to the search component-->
    <search @clicked="updateQueryResult"></search>
    <display
     v-if="active"
     @nextbooks="getNextBooks"
     @previousbooks="getPreviousBooks"
     v-bind:queryResults="queryResult"
     >
     </display>
  </div>
</template>

<script>
/*
  Primitive vs Rerfence Types vue.js

  References change in all components. Whereas Primitive changes only update in that specific component.
*/
// @ is an alias to /src
/*
  We can create data here in the parent, and pass in a prob to the search,
  then we emit the information in the search component, so that the parent
  component receives the information.

  We can then pass the information to a child component, using a boolean if
  statement to make sure it only renders when data exsists.
*/
import axios from 'axios'
import search from '../components/search/'
import display from '../components/display/'
export default {
  name: 'home',
  data () {
    return {
      queryResult: [],
      query: '',
      active: false
    }
  },
  mounted: function () {
    let apiUrl = 'http://127.0.0.1:8000/books/'
    // Mounted is called whenever the object is created
    axios.get(apiUrl).then(response => {
      this.queryResult = response.data.results
      this.active = true
    })
  },
  watch: {
    query () {
      // upon search - filter the results
      let apiUrl = 'http://127.0.0.1:8000/books/'
      // Mounted is called whenever the object is created
      // checks if the query is empty or not.
      if (this.query !== '' || this.query !== null) {
        apiUrl = `http://127.0.0.1:8000/books/?search=${this.query}`
      }
      axios.get(apiUrl).then(response => {
        this.queryResult = response.data.results
        this.active = true
      })
    }
  },
  components: {
    search,
    display
  },
  methods: {
    // called when search.vue emits that the search button has been clicked
    updateQueryResult: function (result) {
      console.log(result)
      this.query = result
      console.log(this.query)
    },
    
  }
}
</script>
