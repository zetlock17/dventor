export interface newApplication {
    login: string,
    password: string,
    name: string,
    surname: string,
    age: number,
    city: string,
    place_of_study: string,
    experience: number,
    company: string,
    post: string,
    descriptiion: string,
    specialization: string,
    stack: string[]
}

export interface application {
    id: number,
    name: string,
    surname: string,
    age: number,
    city: string,
    place_of_study: string,
    experience: number,
    company: string,
    post: string,
    description: string,
    specialization: string,
    stack: string[],
    telegram_username: string,
    status: string,
}