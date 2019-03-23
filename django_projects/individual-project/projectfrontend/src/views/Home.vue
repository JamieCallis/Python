<template>
  <div class="home">
    <!-- Sends the information to the search component-->
    <search @clicked="updateQueryResult"></search>
    <display
     v-if="active" 
     v-bind:queryResults="queryResult" 
     v-bind:tableHeaders="tableHeaders"
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
import search from '../components/search/'
import display from '../components/display/'
export default {
  name: 'home',
  data () {
    return {
      queryResult: [],
      tableHeaders:['word', 'part of speach', 'POS explanation'],
      active: false
    }
  },
  components: {
    search,
    display
  },
  methods: {
    updateQueryResult: function (result) {
      this.queryResult = result
      this.active = true
    }
  }
}
</script>
