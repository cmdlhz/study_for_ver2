<template>
  <v-dialog max-width="600px">
    <v-btn flat slot="activator" class="success">Add a new project</v-btn>
    <v-card>
      <v-card-title>
        <h2>Add a New Project</h2>
      </v-card-title>
      <v-card-text>
        <v-form class="px-3" ref="form">
          <v-text-field label="title" v-model="title" prepend-icon="folder" :rules="titleRules"></v-text-field>
          <v-textarea label="information" v-model="content" prepend-icon="edit" :rules="contentRules"></v-textarea>

          <v-menu>
            <v-text-field :value="formattedDate" slot="activator" label="Due date" prepend-icon="date_range" :rules="dateRules"></v-text-field>
            <v-date-picker v-model="due"></v-date-picker>
          </v-menu>

          <v-spacer></v-spacer>

          <v-btn flat class="success mx-0 mt-3" @click="submit">Add this project</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
  import format from 'date-fns/format'

  export default {
    data(){
      return{
        title: '', 
        content: '',
        due: null,
        titleRules: [
          v => !!v || 'This field is required. Please write a title.',
          v => v.length >= 3 || 'The minimum length is 3 characters'
        ],
        contentRules: [
          v => !!v || 'This field is required. Please add information.',
          v => v.length >= 10 || 'The minimum length is 10 characters'
        ],
        dateRules: [
          v => !!v || 'This field is required. Please select a date.',
        ]
      }
    },
    methods:{
      submit(){
        if(this.$refs.form.validate()){
          alert('You\'ve successfully sumbitted a form!')
        } else {
          alert('The form can\'t be submitted until all fields are filled out.')
        }
      }
    },
    computed:{
      formattedDate(){
        return this.due ? format(this.due, 'MMM D, YYYY') : ''
      }
    }
  }
</script>

<style scoped>

</style>