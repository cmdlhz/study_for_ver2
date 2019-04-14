<template>
  <div class="home">
    <h1>Homepage</h1>
    <v-btn class="blue lighten-1 white--text">CLICK ME</v-btn>
    <v-btn depressed color="blue lighten-1">CLICK ME</v-btn>
    <v-btn flat color="blue lighten-1">CLICK ME</v-btn>

    <v-btn depressed class="blue lighten-1 white--text">
      <v-icon left>email</v-icon>
      <span>EMAIL ME</span>
    </v-btn>
    <v-btn depressed small class="blue lighten-1 white--text">
      <v-icon left small>email</v-icon>
      <span>EMAIL ME</span>
    </v-btn>
    <v-btn large class="blue lighten-1 white--text">
      <span>EMAIL ME</span>
      <v-icon right large>email</v-icon>
    </v-btn>
    <v-btn fab depressed small dark color="red darken-1">
      <v-icon>favorite</v-icon>
    </v-btn>
    <v-btn fab small dark color="red darken-1">
      <v-icon>favorite</v-icon>
    </v-btn>
  </div>
</template>

<script>
  export default {

  }
</script>
