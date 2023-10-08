export enum FetchState {
  DEFAULT = "DEFAULT",
  LOADING = "LOADING",
  SUCCESS = "SUCCESS",
  ERROR = "ERROR",
}

export type PersonasData = {
  ltla_code: string;
  ltla_name: string;
  sex: string;
  ethnicity: string;
  age_category: number;
  notes: number;
  age: number;
  employment: number;
  observation: number;
  headshot_file: string;
};

export type LtlaListData = {
  ltla_code: string;
  ltla_name: string;
};
