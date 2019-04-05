<style lang="scss">
  @import './search.scss';
</style>

<template>
    <form class="search-form">
      <section class="search-container">
        <textarea v-model="query" placeholder="search text here" row="4" cols="50"></textarea>
        <button @click.prevent="searchQuery">search</button>
      </section>
    </form>
</template>

<script>

import axios from 'axios'
export default {
  name: 'search',
  data () {
    return {
      query: '',
      queryResult: [],
      search_term: ''
    },
  mounted: function () {

  },
  methods: {
    async searchQuery () {
      // We want to call the backend sending it a JSON request and CSRF token
      // then handle the response 127.0.0.1:8000
      const response = await axios.post('http://127.0.0.1:8000/spacyapi/query/', {
        message: this.query
      })

      if (response !== undefined) {
        this.queryResult = response.data.result
        this.$emit('clicked', this.queryResult)
      } else {
        console.log('Error, request failed')
      }

      // axios.post('http://127.0.0.1:8000/spacyapi/query/',
      //   {
      //     message: this.query
      //   }
      // ).then(response => {
      //   this.queryResult = response.data.result
      // }).catch(error => {
      //   console.log(error)
      // })
    }
  }
}
</script>
