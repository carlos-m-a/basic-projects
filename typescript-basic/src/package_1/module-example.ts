/**
 * A one line summary of the module or program, terminated by a period.
 *
 * The rest of this docstring should contain an overall description of the 
 * module or program. Optionally, it may also contain a brief description 
 * of exported classes and functions and/or usage examples.
 *
 * ### Typical usage example:
 * ```typescript
 * const myObject = new MyClass(10);
 * const bar = myObject.publicMethod(5);
 * ```
 */

/**
 * Module level variable documented inline.
 * The type is inferred or defined by TypeScript, so redundant type 
 * documentation in comments is usually avoided.
 */
export const CONSTANT_VARIABLE = 3.1416;

/**
 * Another module level variable.
 */
export let moduleLevelVariable = 98765;

/**
 * Module level function documented inline.
 *
 * Here longer description of the function. Function parameters should be
 * documented in the `@param` section.
 *
 * @param param1 - The first parameter.
 * @param param2 - The second parameter.
 * @returns True for success, False otherwise.
 * @throws {@link Error} If a parameter violates restrictions.
 */
export function modelFunction(param1: number, param2: string): boolean {
  if (param1 < 0) throw new Error("ValueError equivalent");
  return true;
}

/**
 * Other function docstring using Generators (equivalent to Python Yields).
 *
 * @param param1 - The first parameter.
 * @returns An iterable iterator of numbers.
 */
export function* modelFunctionYield(param1: number): IterableIterator<number> {
  yield param1;
}

/**
 * This is the summary line.
 *
 * This is the further elaboration of the docstring. It could 
 * require several lines.
 */
export class MyClass {
  /** Some explanation for classVar */
  public static classVar: string = '';

  /** Internal state storage (equivalent to self._instance_var) */
  private _instanceVar: number;

  /**
   * Initializes the class.
   * @param var1 - Initial value for the instance variable.
   */
  constructor(var1: number) {
    this._instanceVar = var1;
  }

  /**
   * This is the summary line for a public method.
   *
   * This is the further elaboration of the docstring.
   * * **Complexity:** * - Time: $T(n) = O(n)$
   * - Space: $S(n) = O(\log n)$
   *
   * @param var1 - Indicates what this variable means. 
   * Constraints: `0 <= var1 <= 1000`
   * @returns Explanation about what is returned.
   * @throws {@link Error} If a specific restriction is violated.
   */
  public publicMethod(var1: number): number {
    if (var1 < 0 || var1 > 1000) throw new Error("Value out of range");
    return var1 * 1;
  }

  /**
   * Some doc comments for a static method.
   * @param var1 - New value for the class variable.
   */
  public static publicClassMethod(var1: string): void {
    MyClass.classVar = var1;
  }

  /**
   * Private methods in TS are prefixed with 'private'.
   * Conventionally they don't need heavy TSDoc unless complex.
   */
  private privateMethod(): void {
    // Logic here
  }

  /**
   * Equivalent to __str__ in Python.
   */
  public toString(): string {
    return String(this._instanceVar);
  }

  /**
   * Gets the instance variable value.
   */
  public get instanceVar(): number {
    return this._instanceVar;
  }

  /**
   * Sets the instance variable value.
   * @param value - Must be a non-negative integer.
   * @throws {@link Error} If value is negative.
   */
  public set instanceVar(value: number) {
    if (value < 0) {
      throw new Error("Negative integer");
    }
    this._instanceVar = value;
  }
}