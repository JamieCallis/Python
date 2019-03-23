<style lang="scss">
    @import './display.scss';
</style>

<template>
  <section class="display-container">
    <table>
      <thead>
        <tr>
          <th v-bind:key="index" v-for="(header, index) in tableHeaders">{{header}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-bind:key="index" v-for="(token, index) in queryResults">
          <td>{{token.word}}</td>
          <td>{{token.pos}}</td>
          <td>{{token.pos_responsing}}</td>
        </tr>
      </tbody>
    </table>
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
    tableHeaders: {
      type: Array,
      required: true
    }
  }
}
</script>
