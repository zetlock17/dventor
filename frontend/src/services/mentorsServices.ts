import { getRequest, type ApiResponse } from './api';
import type { Mentor } from '../types/mentor';

export const getMentors = async (): Promise<ApiResponse<Mentor[]>> => {
  return await getRequest<Mentor[]>('/mentors');
};
