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
export default {
  name: 'search',
  data () {
    return {
      query: ''
    }
  },
  methods: {
    searchQuery: function (event) {
      this.$emit('clicked', this.query)
    }
  }
}
</script>
