export interface newApplication {
    username: string,
    login: string,
    password: string,
    specialization: string,
    experience: string,
}

export interface application {
    id: number,
    login: string,
    password: string,
    username: string,
    specialization: string,
    experience: number,
    telegram_id: string,
    telegram_username: string,
    status: string,
}