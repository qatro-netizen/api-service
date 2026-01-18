// types.ts
export interface User {
  id: number;
  name: string;
  email: string;
}

export interface ErrorResponse {
  code: number;
  message: string;
}

export interface Pagination {
  page: number;
  limit: number;
  total: number;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: Pagination;
}

export interface ApiRequestOptions {
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  url: string;
  headers?: { [key: string]: string };
  data?: any;
}

export interface RequestOptions {
  params?: { [key: string]: string };
  query?: { [key: string]: string };
}