<template>
    <v-card class="mx-auto" width="300">
        <v-img height="200px" :src="props.link" cover></v-img>

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
                   {{props.rese}}
                </v-card-text>
            </div>
        </v-expand-transition>
    </v-card>
</template>

<script setup>
    import { ref, defineProps } from "vue"
    const props = defineProps({
        marca: String,
        modelo: String,
        link: String,
        rese: String
    })

    console.log(props)

    const show = ref(false)
</script>
