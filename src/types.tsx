export enum FetchState {
    DEFAULT = "DEFAULT",
    LOADING = "LOADING",
    SUCCESS = "SUCCESS",
    ERROR = "ERROR",
  }
  
export type PostData = {
    MSOACode: string;
    MSOAName: string;
    LACode: string;
    LAname: string;
    AllAges: number;
    Gender: string;
    age: number;
    ethniticty: string;
  };