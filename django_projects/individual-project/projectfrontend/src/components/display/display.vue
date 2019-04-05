<style lang="scss">
    @import './display.scss';
</style>

<template>
  <section class="display-container">
      <div class="book-card" v-bind:key="book.bookID" v-for="book in queryResults">
        <router-link :to="{name: 'individualbook', params: book}">
          {{book.title}}
        </router-link>
        <p>{{book.author}}</p>
      </div>
      </section>
</template>

<script>
export default {
  name: 'display',
  props: {
    queryResults: {
      type: Array,
      required: true
    },
    
  }
}
</script>
