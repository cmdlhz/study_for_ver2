<template>
  <div class="dashboard">
    <h1 class="subheading grey--text">Dashboard</h1>
    <!-- Add "fluid" full width / smaller margins -->
    <v-container class="my-5">
      <v-layout row wrap>
        <v-flex xs12 md6>
          <v-btn outline block class="primary">ONE</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn outline block class="primary">TWO</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn outline block class="primary">THREE</v-btn>
        </v-flex>
        <v-flex xs4 md2>
          <v-btn outline block class="primary">FOUR</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-space-around>
        <v-flex xs4 md3>
          <v-btn outline block class="success">FIVE</v-btn>
        </v-flex>
        <v-flex xs4 md3>
          <v-btn outline block class="success">SIX</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  export default {

  }
</script>
