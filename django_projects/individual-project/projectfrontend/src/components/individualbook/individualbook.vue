<style lang="scss">
    @import './individualbook.scss';
</style>

<template>
  <section class="book-container" v-if="active">
      <div class="book-template">
        <h1 class="title">{{book.title}}</h1>
        <p class="author">{{book.author}}</p>
        <h3 class="subjects">Subjects</h3>
        <ul class="subject-list">
          <li class="subject" v-bind:key="index" v-for="(item, index) in book.subject">{{item}}</li>
        </ul>
        <h2 class="summary-of-text">Summary of Text</h2>
        <p class="summary">{{bookSummary}}</p>
        <p class="rights">{{book.rights}}</p>
      </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'individualbook',
  data () {
    return {
      book: '',
      bookSummary: '',
      fullText: '',
      active: false
    }
  },
  mounted: function () {
    let apiUrl = ''
    // pre check
    if (this.$route.params.bookID) {
      this.book = this.$route.params
      // We need to then grab the rest of the information
      apiUrl = `http://127.0.0.1:8000/book/bookDetailsQuery/?bookID=${this.book.bookID}`
      axios.get(apiUrl).then(response => {
        this.bookSummary = response.data.bookSummary
      })

      apiUrl = `http://127.0.0.1:8000/books/getBooksSubject/?bookID=${this.book.bookID}`

      axios.get(apiUrl).then(response => {
        this.book.subject = response.data.subject
      })
      this.active = true
    }
  }
}
</script>
