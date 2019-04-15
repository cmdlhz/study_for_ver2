<template>
  <div class="dashboard">
    <h1 class="subheading grey--text">Dashboard</h1>
    <!-- Add "fluid" full width / smaller margins -->
    <v-container class="my-5">
      <v-card flat class="pa-3">
        <v-layout row wrap>
          <v-flex xs12 md6>
            <div class="caption grey--text">PROJECT TITLE</div>
            <div>Create a new website.</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">PERSON</div>
            <div>Jen Lim</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">DUE DATE</div>
            <div>2019/7/31</div>
          </v-flex>
          <v-flex xs2 sm4 md2>
            <div class="caption grey--text">STATUS</div>
            <div>ongoing</div>
          </v-flex>
        </v-layout>
      </v-card>
    </v-container>
  </div>
</template>

<script>
  export default {

  }
</script>
