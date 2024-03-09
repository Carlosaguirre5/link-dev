<template>
    <v-card class="mx-auto" width="300">
        <v-img height="200px" src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" cover></v-img>

        <v-card-title>
            {{ props.marca }}
        </v-card-title>

        <v-card-subtitle>
            {{ props.modelo }}
        </v-card-subtitle>

        <v-card-actions>
            <v-btn color="orange-lighten-2" variant="text">
                Explore
            </v-btn>

            <v-spacer></v-spacer>

            <v-btn color="white" :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
        </v-card-actions>

        <v-expand-transition>
            <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                    I'm a thing. But, like most politicians, he promised more than he could deliver. You
                    won't have time for sleeping, soldier, not with all the bed making you'll be doing.
                    Then we'll go with that data file! Hey, you add a one and two zeros to that or we
                    walk! You're going to do his laundry? I've got to find a way to escape.
                </v-card-text>
            </div>
        </v-expand-transition>
    </v-card>
</template>

<script setup>
    import { ref, defineProps } from "vue"
    const props = defineProps({
        marca: String,
        modelo: String
    })

    const show = ref(false)
</script>
